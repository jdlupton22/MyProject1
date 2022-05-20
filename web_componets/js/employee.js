const table = document.getElementById("reimbursementsTable");
const tableBody = document.getElementById("reimbursementsBody");

async function createReimbursement() {
    const requestId = document.getElementById("requestId").value;
    const empId = document.getElementById("empId").value;
    const evLocation = document.getElementById("evLocation").value;
    const evCost = document.getElementById("evCost").value;
    const evType = document.getElementById("evType").value;
    const description = document.getElementById("description").value;
    const justification = document.getElementById("justification").value;
    const gradingFormat = document.getElementById("gradingFormat").value;
    const grade = document.getElementById("grade").value;
    
    let response = await fetch("http://127.0.0.1:5000/reimbursements", {
        method:"POST",
        mode: "cors",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            "requestId": requestId,
            "empId": empId,
            "evLocation": evLocation,
            "evCost": evCost,
            "evType": evType,
            "description": description,
            "justification": justification,
            "gradingFormat": gradingFormat,
             "grade": grade})
    }
    )
    if (response.status === 200) {
        let body = await response.json();
        alert("Request Submitted Successful!") 
    } else {
        let body = await response.json;
        alert("Request Failed!")
    }
}

async function getMyReimbursementData(){
    let url = "http://127.0.0.1:5000/reimbursement/";
    let response = await fetch(url);

    if (response.status === 200) {
        let body = await response.json();
        populateData(body);
    } else {
        alert("There was a problem trying to get the reimbursement information!")
    }
}

function populateData(responseBody) {
    for (let reimbursements of responseBody) {
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${reimbursements.requestId}</td>
                                <td>${reimbursements.empId}</td>
                                <td>${reimbursements.evLocation}</td>
                                <td>${reimbursements.evCost}</td>
                                <td>${reimbursements.evType}</td>
                                <td>${reimbursements.description}</td>
                                <td>${reimbursements.justification}</td>
                                <td>${reimbursements.gradingFormat}</td>
                                <td>${reimbursements.grade}</td>`
        tableBody.appendChild(tableRow)
    }
}

getMyReimbursementData()

function Logout() {
    sessionStorage.clear()
    window.location.href = "login.html";
}

