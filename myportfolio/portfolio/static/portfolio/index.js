document.addEventListener('DOMContentLoaded', () => {

    fetchSoftSkills();

});



function insertSoftSkill(softSkill) {

    const $div = document.createElement('div');
    $div.classList.add('col-md-4');

    $div.innerHTML = `
        <div class="card special-skill-item border-0">
            <div class="card-header bg-transparent border-0">
                <i class="icon ion-ios-star-outline"></i>
            </div>
            <div class="card-body">
                <h3 class="card-title">${softSkill["name"]}</h3>
                <p class="card-text">${softSkill["description"]}</p>
            </div>
        </div>
    `

    document.getElementById('soft-skills-container').appendChild($div);

}



function insertAlert(error, alertType, container) {

    const $div = document.createElement("div");

    $div.setAttribute("class", `alert alert-${alertType}`);
    $div.innerText = `${error}`;

    document.getElementById(`${container}`).appendChild($div);

}



function fetchSoftSkills() {

    fetch(`soft_skills/get/all/`, {
        method: 'GET',
    })
        .then(response => response.json())
        .then(data => {

            if (data.status == 200) {

                if (data.alert) {

                    insertAlert(data.alert, "warning", "soft-skills-container");

                } else {

                    Object.keys(data).forEach(key => {

                        if (key != "status") {
    
                            insertSoftSkill(data[key]);
    
                        }
    
                    });

                }

            } else if (data.status == 405) {

                insertAlert(data["error"], "danger", "soft-skills-container");

            } else if (data.status == 500) {

                insertAlert(data["error"], "danger", "soft-skills-container");

            } else {

                insertAlert("An unexpected error occurred, please try again.", "warning", "soft-skills-container");

            }

        });

}