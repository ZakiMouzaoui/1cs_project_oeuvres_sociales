function validateForm() {
    var n = document.getElementById('name').value;
    var p = document.getElementById('prenom').value;
    var e = document.getElementById('email').value;
    var s = document.getElementById('subject').value;
    var m = document.getElementById('message').value;
    var onlyLetters =/^[a-zA-Z\s]*$/; 
    var onlyEmail = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    
    
    if(n == "" || n == null){
        document.getElementById('nameLabel').innerHTML = ('veuillez saisir votre nom');
        document.getElementById('name').style.borderColor = "red";
        return false;
    }

    if(p == "" || p == null){
        document.getElementById('prenomLabel').innerHTML = ('Veuillez saisir votre prénom');
        document.getElementById('prenom').style.borderColor = "red";
        return false;
    }
       
  
    if (!n.match(onlyLetters)) {
        document.getElementById('nameLabel').innerHTML = ('Veuillez saisir que des lettres');
        document.getElementById('name').style.borderColor = "red";
        return false;
    }
  
    if(e == "" || e == null ){
          document.getElementById('emailLabel').innerHTML = ('Veuillez saisir votre Email');
          document.getElementById('email').style.borderColor = "red";
          return false;
      }
  
    if (!e.match(onlyEmail)) {
        document.getElementById('emailLabel').innerHTML = ('Veuillez entrer une adresse email valide');
        document.getElementById('email').style.borderColor = "red";
        return false;
    }
  
    if(s == "" || s == null ){
          document.getElementById('subjectLabel').innerHTML = ('Veuillez saisir votre numéro de téléphone');
          document.getElementById('subject').style.borderColor = "red";
          return false;
      }
 
    else{
          return true;
      }
      
}