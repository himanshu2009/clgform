function alertHide(){
    var container = document.getElementsByClassName('error-container');
    container[0].classList.add('d-none');
}
setTimeout(alertHide, 2000);