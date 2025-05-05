  document.querySelectorAll('.password-toggle').forEach(toggle => {
        toggle.addEventListener('click', function() {
            const passwordField = this.previousElementSibling;
            if (passwordField.type === "password") {
                passwordField.type = "text";
                this.querySelector('i.fa-eye').style.display = 'none';
                this.querySelector('i.fa-eye-slash').style.display = 'inline';
            } else {
                passwordField.type = "password";
                this.querySelector('i.fa-eye').style.display = 'inline';
                this.querySelector('i.fa-eye-slash').style.display = 'none';
            }
        });
    });
