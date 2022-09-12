var overlay = document.getElementById('overlay');
var btnClose = document.getElementById('btnClose');
btnClose.addEventListener('click',closePopup)
function closePopup(){
    overlay.style.display = 'none';
}