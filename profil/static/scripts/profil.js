document.addEventListener('DOMContentLoaded', function () {
    const editBtn = document.getElementById('edit-btn');
    const editForm = document.getElementById('edit-form');

    editBtn.addEventListener('click', function (event) {
        event.preventDefault();
        editForm.style.display = 'block';
    });
});
