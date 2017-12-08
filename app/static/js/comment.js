var link = document.getElementById('deleteLink');
var form = document.getElementById('deleteForm');

console.log('link', link);
console.log('form', form);

function linkClick() {
  console.log('Diste click al link');
  form.submit();
}

link.onclick = linkClick;
