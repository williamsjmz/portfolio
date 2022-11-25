document.addEventListener("DOMContentLoaded", (e) => {

    fetchExperiences();

    fetchTechnologies();

});


function fetchExperiences() {

    fetch(`get/all/experiences/`, {

        method: 'GET',

    })
        .then(response => response.json())
        .then(data => {

            if (data.status == 200) {

                if (data.alert) {

                    insertAlert(data.alert,  "educations-container", "warning");

                } else {

                    Object.keys(data).forEach(key => {

                        if (key != "status") {
        
                            insertExperience(data[key]);
        
                        }
        
                    });

                }

            } else if (data.status == 405) {

                insertAlert(data["error"],  "educations-container", "danger");

            } else if (data.status == 500) {

                insertAlert(data["error"],  "educations-container", "danger");

            } else {

                insertAlert("Ocurrió un error inesperado, intentalo de nuevo.",  "educations-container", "warning");

            }

        })

}



function fetchTechnologies() {

    fetch(`get/all/technologies/`, {

        method: 'GET',

    })
    .then(response => response.json())
    .then(data => {

        console.log(data)

        if (data.status == 200) {

            if (data.alert) {

                insertAlert(data.message, "technologies-container", "warning");

            } else {

                data.technologies.forEach(technology => {

                    insertTechnology(technology);

                });

            }

        } else if (data.status == 405) {

            insertAlert(data.message, "technologies-container", "danger");

        } else if (data.status == 500) {

            insertAlert(data.message, "technologies-container", "danger");

        } else {

            insertAlert("Ocurrió un error inesperado, intentalo de nuevo.",  "technologies-container", "warning");

        }

    })

}



function insertExperience(experience) {

    if (experience.is_work) {

        const $div = document.createElement("div");
        $div.classList.add("item");

        $div.innerHTML = `
        
        <div class="row">
        <div class="col-md-6">
            <h3>${experience.title}</h3>
            <h4 class="organization">${experience.name}</h4>
        </div>
        <div class="col-md-6"><span class="period">${experience.start_date} - ${experience.end_date}</span></div>
        </div>
        <p class="text-muted">${experience.description}</p>
        
        `;

        document.getElementById('works-container').appendChild($div);

    } else {

        const $div = document.createElement("div");
        $div.classList.add("item");

        $div.innerHTML = `
        
        <div class="row">
        <div class="col-md-6">
            <h3>${experience.title}</h3>
            <h4 class="organization">${experience.name}</h4>
        </div>
        <div class="col-6"><span class="period">${experience.start_date} - ${experience.end_date}</span></div>
        </div>
        <p class="text-muted">${experience.description}</p>

        `;

        document.getElementById('educations-container').appendChild($div);

    }

}



function insertTechnology(technology) {

    const $div = document.createElement("div");

    $div.innerHTML = `
    <h3>${technology.name}</h3>
    <div class="progress">
        <div class="progress-bar" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100" style="width: ${technology.domination}%;"><span class="visually-hidden">100%</span></div>
    </div>
    `;

    document.getElementById("technologies-container").appendChild($div);

}



function insertAlert(error, containerID, alertType) {

    const $div = document.createElement("div");

    $div.setAttribute("class", `alert alert-${alertType}`);
    $div.innerText = `${error}`;

    const $headings = document.querySelectorAll(".experience-heading");
    $headings.forEach((heading) => {

        heading.style.display = 'none';

    })

    document.getElementById(`${containerID}`).appendChild($div);

    const $alertHeading = document.getElementById('alert-experiences-heading');
    $alertHeading.style.display = 'block';

}