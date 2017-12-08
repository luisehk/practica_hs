var form = document.getElementById('deleteForm');
var commentId = document.getElementById('commentId');

function deleteComment(id) {
  commentId.value = id;
  form.submit();
}
