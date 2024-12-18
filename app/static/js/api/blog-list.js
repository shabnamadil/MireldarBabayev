const BASE_URL = `${location.origin}/api/blogs/`;
const BLOG_PAGE_URL = `${location.origin}/blogs/`;
const blogsContainer = document.getElementById('blogs');
const filterResults = document.getElementById('filterResults');
const searchQuery = document.getElementById('query-word');
const searchIcon = document.getElementById('searchIcon');
const clearFilterButton = document.getElementById('clearfilter');
const nextBlogs = document.getElementById('nextBlogs');
const previousBlogs = document.getElementById('previousBlogs');

const BlogListTranslations = {
    en: "Read More",
    az: "Daha çox",
    ru: "Читать далее"
};

let currentPage = 1;
let currentCategory = null;
let currentTag = null;
let currentQuery = '';

document.addEventListener('DOMContentLoaded', async function () {
    const urlParams = new URLSearchParams(window.location.search);
    const categorySlug = urlParams.get('category');
    const tagSlug = urlParams.get('tag');
    currentCategory = categorySlug;
    currentTag = tagSlug;

    // Fetch and render blogs based on URL params or default
    await loadBlogs();

    // Event listener for search functionality
    searchIcon.addEventListener('click', handleSearch);
    searchQuery.addEventListener('keypress', handleSearchOnEnter);
    clearFilterButton.addEventListener('click', clearFilter);
    nextBlogs.addEventListener('click', handleNextBlogs);
    previousBlogs.addEventListener('click', handlePreviousBlogs);

    document.querySelectorAll('.category-link').forEach(link => {
        link.addEventListener('click', async (event) => {
            event.preventDefault();
            const categorySlug = event.target.dataset.categorySlug;
            const categoryName = event.target.dataset.categoryName;
    
            currentCategory = categorySlug;
            currentTag = null;  // Reset tag filter
            currentQuery = '';  // Reset search query
            currentPage = 1;  // Reset to the first page when a new category is selected
    
            await loadBlogs();  // Fetch and render blogs based on new category
            displayFilterResults(categoryName);
        });
    });
    
    document.querySelectorAll('.tag-link').forEach(link => {
        link.addEventListener('click', async (event) => {
            event.preventDefault();
            const tagSlug = event.target.dataset.tagSlug;
            const tagName = event.target.dataset.tagName;
    
            currentTag = tagSlug;
            currentCategory = null;  // Reset category filter
            currentQuery = '';  // Reset search query
            currentPage = 1;  // Reset to the first page when a new tag is selected
    
            await loadBlogs();  // Fetch and render blogs based on new tag
            displayFilterResults(tagName);
        });
    });
    
});

// Load blogs based on current filters (category, tag, or query)
async function loadBlogs() {
    let blogs;
    if (currentCategory) {
        blogs = await filterBlogsByCategory(currentCategory);
    } else if (currentTag) {
        blogs = await filterBlogsByTag(currentTag);
    } else if (currentQuery) {
        blogs = await filterBlogsByQuery(currentQuery);
    } else {
        blogs = await fetchBlogs(currentPage);
    }

    if (blogs) renderBlogs(blogs);
}

// Handle search on icon click
async function handleSearch() {
    if (searchQuery.value) {
        currentTag = ''
        currentCategory = ''
        currentQuery = searchQuery.value;
        currentPage = 1; // Reset to the first page when performing a new search
        await loadBlogs();
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

// Handle next blogs
async function handleNextBlogs() {
    currentPage++;  // Increment the page
    await loadBlogs();  // Load next page of blogs
}

// Handle previous blogs
async function handlePreviousBlogs() {
    if (currentPage > 1) {
        currentPage--;  // Decrement the page
        await loadBlogs();  // Load previous page of blogs
    }
}

// Fetch blogs function
async function fetchBlogs(currentPage) {
    try {
        const url = new URL(BASE_URL);
        url.searchParams.set('page', currentPage);
        if (currentCategory) url.searchParams.set('category', currentCategory);
        if (currentTag) url.searchParams.set('tag', currentTag);

        const response = await fetch(url);
        if (!response.ok) throw new Error('Failed to fetch blogs');
        const data = await response.json();

        // Handle pagination visibility
        nextBlogs.style.display = data.has_next ? 'block' : 'none';
        previousBlogs.style.display = data.has_previous ? 'block' : 'none';

        return data.results; // Return only the blogs (excluding pagination data)
    } catch (error) {
        console.error('Error fetching blogs:', error);
        return null;
    }
}

// Filter blogs by category
async function filterBlogsByCategory(category) {
    try {
        const response = await fetch(`${BASE_URL}?category=${category}&page=${currentPage}`);
        if (!response.ok) throw new Error('Failed to fetch filtered blogs');
        
        const data = await response.json();

        // Handle pagination visibility
        nextBlogs.style.display = data.has_next ? 'block' : 'none';
        previousBlogs.style.display = data.has_previous ? 'block' : 'none';

        displayClearFilterButton()

        return data.results; // Return only the filtered results
    } catch (error) {
        console.error('Error fetching filtered blogs:', error);
        return null;
    }
}

// Filter blogs by tag
async function filterBlogsByTag(tag) {
    try {
        const response = await fetch(`${BASE_URL}?tag=${tag}&page=${currentPage}`);
        if (!response.ok) throw new Error('Failed to fetch filtered by tag blogs');
        const data = await response.json();

        // Handle pagination visibility
        nextBlogs.style.display = data.has_next ? 'block' : 'none';
        previousBlogs.style.display = data.has_previous ? 'block' : 'none';

        displayClearFilterButton()

        return data.results;
    } catch (error) {
        console.error('Error fetching filtered by tag blogs:', error);
        return null;
    }
}

// Filter blogs by query
async function filterBlogsByQuery(query) {
    try {
        const response = await fetch(`${BASE_URL}?q=${query}&page=${currentPage}`);
        if (!response.ok) throw new Error('Failed to fetch filtered by query blogs');
        const data = await response.json();

        // Handle pagination visibility
        nextBlogs.style.display = data.has_next ? 'block' : 'none';
        previousBlogs.style.display = data.has_previous ? 'block' : 'none';

        displayClearFilterButton()

        return data.results;
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

// Function to get the translation
function translateBlogListLang(key, lang = 'en') {
    return BlogListTranslations[lang] || BlogListTranslations['en'];
}

// Append blogs (adds more content to the existing list)
function appendBlogs(blogs) {
    const blogsHTML = blogs.map(blog => {
        const publishedDate = new Date(blog.published_date);
        const day = publishedDate.getDate().toString().padStart(2, '0');
        const month = publishedDate.toLocaleString('en-US', { month: 'short' }).toUpperCase();
        const truncatedTitle = truncateText(blog.title, 60);
        const urlPath = window.location.pathname;
        const userLang = urlPath.split('/')[1];

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
                    <a href="${BLOG_PAGE_URL}${blog.slug}" class="btn btn-primary">${translateBlogListLang('read_more', userLang)}</a>
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
        filterResults.classList.remove('d-none')
        filterResults.innerHTML = `Results for <i>"${query}"</i>`;
    }
}

// Clear filters
function clearFilter() {
    clearFilterButton.classList.add('d-none');
    filterResults.classList.add('d-none');
    currentCategory = null;
    currentTag = null;
    currentQuery = '';
    searchQuery.value = '';
    currentPage = 1;  // Reset to the first page
    loadBlogs();
}

function displayClearFilterButton () {
    clearFilterButton.classList.remove('d-none')
}