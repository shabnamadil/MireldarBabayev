const COMMENT_URL = `${location.origin}/api/comment/?blog=${blogId}`;
const commentsContainer = document.getElementById('comments');
const commentInputField = document.getElementById('comment-input-field');


// Load comments on page load
document.addEventListener('DOMContentLoaded', async function () {
    await fetchComments();
});

// Fetch all comments
async function fetchComments() {
    try {
        const response = await fetch(COMMENT_URL);
        if (!response.ok) throw new Error('Failed to fetch comments');

        const comments = await response.json();
        renderComments(comments);
    } catch (error) {
        console.error('Error fetching comments:', error);
    }
}

// Render comments (clear and reload)
function renderComments(comments) {
    commentsContainer.innerHTML = '';

    const h3 = document.createElement('h3');
    h3.textContent = `${gettext('Comments')}(${comments.length})`;
    commentsContainer.appendChild(h3);

    appendComments(comments);
}

// Append comments to the DOM
function appendComments(comments) {
    if (!Array.isArray(comments)) {
        console.error('Comments data is not an array:', comments);
        return;
    }

    const commentsHTML = comments.map(comment => createCommentHTML(comment)).join('');
    const commentsList = document.createElement('div');
    commentsList.innerHTML = commentsHTML;

    commentsContainer.appendChild(commentsList);
}

// Create comment HTML
function createCommentHTML(comment) {
    const isAuthor = comment.is_author;
    return `
        <div class="media comment" id="comment-${comment.id}">
            <div>
                <img src="${comment.author_photo}" 
                    alt="${comment.author_full_name || 'Anonymous'}" 
                    class="comment-author-img">
            </div>
            <div class="media-body">
                <div class="comment-header">
                    <p class="comment-author-name">
                        <i class="fas fa-user-circle"></i> ${comment.author_full_name}
                    </p>
                    <p class="comment-date">${comment.created_date}</p>
                </div>
                <p class="comment-content">${comment.content}</p>
                ${
                    isAuthor
                        ? `<div class="comment-actions">
                               <button class="edit" onclick="editComment(${comment.id})">
                                   <i class="fas fa-edit"></i> ${gettext('Edit')}
                               </button>
                               <button class="delete" onclick="deleteComment(${comment.id})">
                                   <i class="fas fa-trash-alt"></i> ${gettext('Delete')}
                               </button>
                           </div>`
                        : ''
                }
            </div>
        </div>
    `;
}

// Add new comment
async function sendComment() {
    const content = commentInputField.value.trim();

    try {
        const response = await fetch(`${location.origin}/api/comment/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken(),
            },
            body: JSON.stringify({
                blog: blogId,
                content: content,
            }),
        });

        if (!response.ok) throw new Error('Failed to post comment');

        const newComment = await response.json();
        addCommentToDOM(newComment);

        commentInputField.value = '';
    } catch (error) {
        console.error('Error posting comment:', error);
    }
}

// Add comment to the DOM
function addCommentToDOM(comment) {
    const commentHTML = createCommentHTML(comment);
    const commentsList = commentsContainer.querySelector('div:last-of-type');

    const commentHeader = commentsContainer.querySelector('h3');
    const currentCount = parseInt(commentHeader.textContent.match(/\d+/)[0]);
    commentHeader.textContent = `${gettext('Comments')} (${currentCount + 1})`;

    if (commentsList) {
        commentsList.innerHTML = commentHTML + commentsList.innerHTML;
    } else {
        appendComments([comment]);
    }
}

// Delete comment
function deleteComment(commentId) {
    commentToDeleteId = commentId; // Store the ID of the comment to delete
    const modal = document.getElementById('deleteCommentModal');
    modal.style.display = 'flex'; // Show the modal
}

// Confirm delete action
document.getElementById('confirmDeleteButton').addEventListener('click', async function () {
    if (!commentToDeleteId) return;

    try {
        const response = await fetch(`${location.origin}/api/comment/${commentToDeleteId}/`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': getCSRFToken(),
            },
        });

        if (!response.ok) throw new Error('Failed to delete comment');

        removeCommentFromDOM(commentToDeleteId);
        closeModal();
    } catch (error) {
        console.error(`Error deleting comment ${commentToDeleteId}:`, error);
        alert(gettext('Failed to delete comment. Please try again.'));
    }
});

// Cancel delete action
document.getElementById('cancelDeleteButton').addEventListener('click', function () {
    closeModal();
});

// Close the modal
function closeModal() {
    const modal = document.getElementById('deleteCommentModal');
    modal.style.display = 'none'; // Hide the modal
    commentToDeleteId = null; // Clear the stored comment ID
}

// Remove comment from the DOM
function removeCommentFromDOM(commentId) {
    const commentElement = document.getElementById(`comment-${commentId}`);
    if (commentElement) {
        commentElement.remove();
    }

    const commentHeader = commentsContainer.querySelector('h3');
    const currentCount = parseInt(commentHeader.textContent.match(/\d+/)[0], 10);
    commentHeader.textContent = `${gettext('Comments')} (${Math.max(0, currentCount - 1)})`;
}

// Edit comment
function editComment(commentId) {
    const commentElement = document.getElementById(`comment-${commentId}`);
    const contentElement = commentElement.querySelector('.comment-content');
    const originalContent = contentElement.textContent.trim();

    const editTextarea = document.createElement('textarea');
    editTextarea.className = 'edit-comment-textarea';
    editTextarea.value = originalContent;

    contentElement.replaceWith(editTextarea);

    const actions = commentElement.querySelector('.comment-actions');
    actions.innerHTML = `
        <button class="save" onclick="saveComment(${commentId})">
            <i class="fas fa-save"></i> ${gettext('Save')}
        </button>
        <button class="cancel" onclick="cancelEditComment(${commentId}, '${originalContent}')">
            <i class="fas fa-times"></i> ${gettext('Cancel')}
        </button>
    `;
}

// Save edited comment
async function saveComment(commentId) {
    const commentElement = document.getElementById(`comment-${commentId}`);
    const editTextarea = commentElement.querySelector('.edit-comment-textarea');
    const updatedContent = editTextarea.value.trim();

    if (!updatedContent) {
        alert(gettext('Comment content cannot be empty.'));
        return;
    }

    try {
        const response = await fetch(`${location.origin}/api/comment/${commentId}/`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken(),
            },
            body: JSON.stringify({ content: updatedContent }),
        });

        if (!response.ok) throw new Error('Failed to update comment');

        const updatedComment = await response.json();
        updateCommentInDOM(commentId, updatedComment);
    } catch (error) {
        console.error(`Error updating comment ${commentId}:`, error);
        alert(gettext('Failed to update comment. Please try again.'));
    }
}

// Update comment in the DOM
function updateCommentInDOM(commentId, comment) {
    const commentElement = document.getElementById(`comment-${commentId}`);
    const editTextarea = commentElement.querySelector('.edit-comment-textarea');

    const updatedContentElement = document.createElement('p');
    updatedContentElement.className = 'comment-content';
    updatedContentElement.textContent = comment.content;
    editTextarea.replaceWith(updatedContentElement);

    const actions = commentElement.querySelector('.comment-actions');
    actions.innerHTML = `
        <button class="edit" onclick="editComment(${commentId})">
            <i class="fas fa-edit"></i> ${gettext('Edit')}
        </button>
        <button class="delete" onclick="deleteComment(${commentId})">
            <i class="fas fa-trash-alt"></i> ${gettext('Delete')}
        </button>
    `;
}

// Cancel editing comment
function cancelEditComment(commentId, originalContent) {
    const commentElement = document.getElementById(`comment-${commentId}`);
    const editTextarea = commentElement.querySelector('.edit-comment-textarea');

    const originalContentElement = document.createElement('p');
    originalContentElement.className = 'comment-content';
    originalContentElement.textContent = originalContent;
    editTextarea.replaceWith(originalContentElement);

    const actions = commentElement.querySelector('.comment-actions');
    actions.innerHTML = `
        <button class="edit" onclick="editComment(${commentId})">
            <i class="fas fa-edit"></i> ${gettext('Edit')}
        </button>
        <button class="delete" onclick="deleteComment(${commentId})">
            <i class="fas fa-trash-alt"></i> ${gettext('Delete')}
        </button>
    `;
}

// Get CSRF token
function getCSRFToken() {
    const csrfCookie = document.cookie.split('; ').find(row => row.startsWith('csrftoken='));
    return csrfCookie ? csrfCookie.split('=')[1] : '';
}
