function analyzeResume() {

    const resume = document.getElementById("resume").files[0];
    const jobDescription =
        document.getElementById("jobDescription").value;

    if (!resume) {
        alert("Please upload your resume.");
        return;
    }

    if (!jobDescription.trim()) {
        alert("Please enter the job description.");
        return;
    }

    document.getElementById("score").innerText =
        "Match Score: Analyzing...";

    document.getElementById("skills").innerHTML =
        `
        <p>Resume uploaded: ${resume.name}</p>
        <p>Job description received.</p>
        <p>AI analysis will be connected next.</p>
        `;
}
