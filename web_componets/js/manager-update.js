const table = document.getElementById("reimbursementStatusTable");
const tableBody = document.getElementById("reimbursementStatusBody");

async function updateReimbursement() {
    const requestId = document.getElementById("requestId").value;
    const projectAward = document.getElementById("projectAward").value;
    const urgent = document.getElementById("urgent").value;
    const status = document.getElementById("status").value;
    const stage = document.getElementById("stage").value;
    const requestDateTime = document.getElementById("requestDateTime").value;
    

    let url = "http://127.0.0.1:5000/reimbursement/"
    let response = await fetch(url + requestId, {
        method: "PATCH",
        mode: "cors",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            "requestId": requestId,
            "projectAward": projectAward,
            " urgent":  urgent,
            "status": status,
            "stage": stage,
            "requestDateTime": requestDateTime
        })
    })

    if (response.status === 200) {
        let body = await response.json();
        alert("Request Updated Successful!")
    } else {
        let body = await response.json;
        alert("Update Request Failed!")
    }
}


async function getAllReimbursementData() {
    let url = "http://127.0.0.1:5000/reimbursements";
    let response = await fetch(url);

    if (response.status === 200) {
        let body = await response.json();
        populateData(body);
    } else {
        alert("There was a problem trying to get the reimbursement information!")
    }
}

function populateData(responseBody) {
    for (let reimbursement_status of responseBody) {
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${reimbursement_status.requestId}</td>
                                <td>${reimbursement_status.projectAward}</td>
                                <td>${reimbursement_status. urgent}</td>
                                <td>${reimbursement_status.status}</td>
                                <td>${reimbursement_status.stage}</td>
                                <td>${reimbursement_status.requestDateTime}</td>`
        tableBody.appendChild(tableRow)
    }
}

getAllReimbursementData()

function Logout() {
    sessionStorage.clear()
    window.location.href = "login.html";
}
