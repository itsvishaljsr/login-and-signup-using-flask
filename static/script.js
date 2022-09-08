var check = function() {

    if (document.getElementById('password').value == document.getElementById('checkPassword').value) {
            document.getElementById("signupbtn").disabled = false;
            document.getElementById('signupbtn').style.backgroundColor = '#3498db';
            document.getElementById('alertPassword').style.color = '#8CC63E';
            document.getElementById('alertPassword').innerHTML = '<span><i class="fas fa-check-circle"></i>Match !</span>';
    } 
    else {
            document.getElementById("signupbtn").disabled = true;
            document.getElementById('signupbtn').style.backgroundColor = '#3498db96';
            document.getElementById('alertPassword').style.color = '#EE2B39';
            document.getElementById('alertPassword').innerHTML = '<span><i class="fas fa-exclamation-triangle"></i>not matching</span>';
    }
}