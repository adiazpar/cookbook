document.querySelectorAll(".nav-item").forEach((item) => {
    if (item.href === window.location.href) {
        item.classList.add("active");
        item.setAttribute("aria-current", "page");
    }
});