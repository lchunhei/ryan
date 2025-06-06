$(document).ready(function(){
    // When the modal is shown
    $('#deleteConfirmModal').on('show.bs.modal', function(event) {
    const button = $(event.relatedTarget);
    const contactId = button.data('id');

    //  vue, anu , react    Update modal content
    $('#modal-contact-id').text(contactId);

    // Set the delete URL
    const deleteUrl = `{% url 'contacts:delete_contact' 0 %}`.replace(
        '0',
        contactId);
    $('#confirmDeleteBtn'),attr('href', deleteUrl);
});

// When delete button is clicked
$('#confirmDeleteBtn').click(function (e) {
    // Close the modal
    $('#deleteConfirmModal').modal('hide');

    // Optional: Add a small delay to let the modal close before redirecting
    setTimeout(function(){
        window.location.href = $('#confirmDeleteBtn').attr('href');}, 300);
    });
})
