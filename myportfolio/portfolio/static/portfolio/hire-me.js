document.addEventListener("DOMContentLoaded", (e) => {

    addButtonsEventListeners();

    const $hireMeBtn = document.getElementById("hire-me-btn");

    $hireMeBtn.addEventListener("click", (e) => {

        document.getElementById("form-alert-danger").style.display = 'none';
        document.getElementById("form-alert-success").style.display = 'none';

        sendEmail(e.target);

    });

});



function addButtonsEventListeners() {

    const $fields = document.querySelectorAll(".hire-me-form-field");

    $fields.forEach(($field) => {

        $field.onkeyup = (e) => {
        
            activateDeactivateButton($fields);

            if ($field.id == "email") {

                validateEmail($field.value);

            }
            
        };

    });

}



function activateDeactivateButton($fields) {

    let count = 0;

    $fields.forEach(($field) => {

        if ($field.value != '') {

            count++;

        }

    });

    if (count == 3) {

        document.getElementById("hire-me-btn").disabled = false;

    } else {

        document.getElementById("hire-me-btn").disabled = true;

    }

}



function sendEmail($hireMeBtn) {

    const $form = document.getElementById("hire-me-form");

    if ($form.classList.contains("valid")) {


        const subject = document.getElementById("subject").value;
        const email = document.getElementById("email").value;
        const message = document.getElementById("message").value;
    
        console.log(subject);
        console.log(email);
        console.log(message);
    
    
        fetch(`send_email/`, {
    
            method: 'POST',
            body: JSON.stringify({
    
                subject: subject,
                email: email,
                message: message
    
            }),
    
        })
        .then(response => response.json())
        .then(result => {
    
            if (result["status"] == 201) {

                showAlert("success", result["message"]);

                clearFields("success");

            }
    
        })

    } else {

        showAlert("danger", "Please enter a valid email address.");

        clearFields("danger");

    }

    $hireMeBtn.disabled = true;

}



function validateEmail(email) {

    const $form = document.getElementById("hire-me-form");

    let regExp = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

    if (email.match(regExp)) {

        $form.classList.add("valid");
        $form.classList.remove("invalid");

    } else {

        $form.classList.add("invalid");
        $form.classList.remove("valid");

    }

}



function showAlert(type, message) {

    
    const $alert = document.getElementById(`form-alert-${type}`);

    $alert.setAttribute("style", "display: block;");
    $alert.innerText = `${message}`;

}



function clearFields(type) {

    const $fields = document.querySelectorAll(".hire-me-form-field");

    $fields.forEach(($field) => {

        if (type == "success") {

            $field.value = "";
        
        } else if (type == "danger") {

            if ($field.id == "email") {

                $field.value = "";

            }

        } else {

            $field.value = "";

        }

    });

}