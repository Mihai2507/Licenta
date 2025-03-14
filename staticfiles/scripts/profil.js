document.addEventListener('DOMContentLoaded', function () {
    const editBtn = document.getElementById('edit-btn');
    const editForm = document.getElementById('edit-form');

    // Când apesi pe butonul de editare, arată formularul de editare
    editBtn.addEventListener('click', function (event) {
        event.preventDefault(); // Previne comportamentul default al linkului
        editForm.style.display = 'block'; // Afișează formularul de editare
    });
});
