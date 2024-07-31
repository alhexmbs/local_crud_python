$(document).ready(function() {
    var deleteUrl;
    $('.delete-btn').on('click', function(event) {
      event.preventDefault();
      deleteUrl = $(this).attr('href');
      $('#confirmDeleteModal').modal('show');
    });

    $('#deleteForm').on('submit', function(event) {
      event.preventDefault();
      $.post(deleteUrl, $(this).serialize(), function() {
        window.location.reload();
      });
    });
  });