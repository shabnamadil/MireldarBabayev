const BASE_URL = `${location.origin}/api/blogs/`;
const BLOG_PAGE_URL = `${location.origin}/blogs/`;
const blogsContainer = document.getElementById('blogs');
const filterResults = document.getElementById('filterResults');
const searchQuery = document.getElementById('query-word');
const searchIcon = document.getElementById('searchIcon');
const clearFilterButton = document.getElementById('clearfilter');
const loadMoreBtn = document.getElementById('loadMoreBtn');

let currentPage = 1;

document.addEventListener('DOMContentLoaded', async function () {
    const urlParams = new URLSearchParams(window.location.search);
    const categorySlug = urlParams.get('category');
    const tagSlug = urlParams.get('tag');

    // Fetch and render blogs based on URL params
    if (categorySlug) {
        const filteredBlogs = await filterBlogsByCategory(categorySlug);
        if (filteredBlogs) renderBlogs(filteredBlogs);
    } else if (tagSlug) {
        const filteredBlogs = await filterBlogsByTag(tagSlug);
        if (filteredBlogs) renderBlogs(filteredBlogs);
    } else {
        const blogs = await fetchBlogs(currentPage);
        if (blogs) renderBlogs(blogs);
    }

    // Event listener for search functionality
    searchIcon.addEventListener('click', handleSearch);
    searchQuery.addEventListener('keypress', handleSearchOnEnter);
    clearFilterButton.addEventListener('click', clearFilter);
    loadMoreBtn.addEventListener('click', handleLoadMore)

    // Category filter event listeners
    document.querySelectorAll('.category-link').forEach(link => {
        link.addEventListener('click', async (event) => {
            event.preventDefault();
            const categorySlug = event.target.dataset.categorySlug;
            const categoryName = event.target.dataset.categoryName;

            const filteredBlogs = await filterBlogsByCategory(categorySlug);
            if (filteredBlogs) renderBlogs(filteredBlogs);
            
            displayFilterResults(categoryName);
        });
    });

    // Tag filter event listeners
    document.querySelectorAll('.tag-link').forEach(link => {
        link.addEventListener('click', async (event) => {
            event.preventDefault();
            const tagSlug = event.target.dataset.tagSlug;
            const tagName = event.target.dataset.tagName;

            const filteredBlogs = await filterBlogsByTag(tagSlug);
            if (filteredBlogs) renderBlogs(filteredBlogs);

            displayFilterResults(tagName);
        });
    });
});

// Handle search on icon click
async function handleSearch() {
    if (searchQuery.value) {
        const filteredBlogs = await filterBlogsByQuery(searchQuery.value);
        if (filteredBlogs) renderBlogs(filteredBlogs);
        displayFilterResults(searchQuery.value);
        searchQuery.value = '';  // Clear search input after search
    }
}

// Handle search on "Enter" key press
async function handleSearchOnEnter(event) {
    if (event.key === 'Enter') {  // Check if "Enter" key is pressed
        event.preventDefault();  // Prevent form submission if inside a form
        await handleSearch();
    }
}

// Handle load more
async function handleLoadMore() {
    currentPage++;  // Increment the page number
    const moreBlogs = await fetchBlogs(currentPage);
    if (moreBlogs && moreBlogs.length > 0) {
        appendBlogs(moreBlogs);
    } else {
        loadMoreBtn.style.display = 'none';  // Hide button if no more blogs
    }
}

// Fetch blogs function
async function fetchBlogs(currentPage) {
    try {
        const response = await fetch(`${BASE_URL}?p=${currentPage}`);
        if (!response.ok) throw new Error('Failed to fetch blogs');
        return await response.json();
    } catch (error) {
        console.error('Error fetching blogs:', error);
        return null;
    }
}

// Filter blogs by category
async function filterBlogsByCategory(category) {
    try {
        const response = await fetch(`${BASE_URL}?category=${category}`);
        if (!response.ok) throw new Error('Failed to fetch filtered by category blogs');
        return await response.json();
    } catch (error) {
        console.error('Error fetching filtered by category blogs:', error);
        return null;
    }
}

// Filter blogs by tag
async function filterBlogsByTag(tag) {
    try {
        const response = await fetch(`${BASE_URL}?tag=${tag}`);
        if (!response.ok) throw new Error('Failed to fetch filtered by tag blogs');
        return await response.json();
    } catch (error) {
        console.error('Error fetching filtered by tag blogs:', error);
        return null;
    }
}

// Filter blogs by query
async function filterBlogsByQuery(query) {
    try {
        const response = await fetch(`${BASE_URL}?q=${query}`);
        if (!response.ok) throw new Error('Failed to fetch filtered by query blogs');
        return await response.json();
    } catch (error) {
        console.error('Error fetching filtered by query blogs:', error);
        return null;
    }
}

// Render blogs (replaces the existing content)
function renderBlogs(blogs) {
    blogsContainer.innerHTML = '';
    appendBlogs(blogs);
}

// Append blogs (adds more content to the existing list)
function appendBlogs(blogs) {
    const blogsHTML = blogs.map(blog => {
    const publishedDate = new Date(blog.published_date);
    const day = publishedDate.getDate().toString().padStart(2, '0');
    const month = publishedDate.toLocaleString('en-US', { month: 'short' }).toUpperCase();
    const truncatedTitle = truncateText(blog.title, 60);

    return `
        <div class="blog-list">
            <img src="${blog.image}" class="img-fluid" alt="${blog.title}">
            <div class="blog-date">
                <h3>${day}</h3>
                <span>${month}</span>
            </div>
            <div class="blog-text-wrap">
                <div class="blog-comment-top">
                    <p><i class="far fa-user"></i>${blog.author} <span>|</span> 
                    <i class="far fa-eye"></i>${blog.view_count} <span>|</span> 
                    <i class="far fa-comment"></i>${blog.comment_count}</p>
                    <label>${blog.category[0]}</label>
                </div>
                <h3>${truncatedTitle}</h3>
                <p>${blog.short_description}</p>
                <a href="${BLOG_PAGE_URL}${blog.slug}" class="btn btn-primary">Read More</a>
            </div>
        </div>
    `;
    }).join('');
    blogsContainer.innerHTML = blogsHTML;  // Append new blogs to the container
}

// Truncate text
function truncateText(text, maxLength) {
    return text.length > maxLength ? text.slice(0, maxLength) + '...' : text;
}

// Display filter results
function displayFilterResults(query) {
    if (filterResults) {
        filterResults.innerHTML = `Results for <i>"${query}"</i>`;
        clearButtonAdd()
    }
}

// Clear filter and reset search results
async function clearFilter() {
    const blogs = await fetchBlogs();
    if (blogs) renderBlogs(blogs);
    resetFilterResults();
}

// Reset search results display
function resetFilterResults() {
    if (filterResults) {
        filterResults.innerHTML = ''; // Clear filter results
    }
    clearButtonRemove()
}

//Clear button add
function clearButtonAdd() {
    clearFilterButton.classList.remove('d-none');  // Show clear filter button
}

//Clear button Remove
function clearButtonRemove() {
    clearFilterButton.classList.add('d-none');  //Clear filter button
}