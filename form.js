function validate() {
    if (document.getElementById('fname').value == '') {
        alert("Please Provide First Name");
        document.getElementById('fname').focus();
        return false;

    } else if (document.getElementById('lname').value == '') {
        alert("Please Provide Last Name");
        document.getElementById('lname').focus();
        return false;
    } else if (document.getElementById('email').value == '') {
        alert("Please enter your email");
        document.getElementById('email').focus();
        return false;
    } else if (document.getElementById('goal').value == '') {
        alert("Please leave a comment");
        document.getElementById('goal').focus();
        return false;

    }

}
