async function analyzeResume() {

    const resumeInput = document.getElementById("resume");
    const jobDescription =
        document.getElementById("jobDescription").value;

    const result = document.getElementById("result");
    const score = document.getElementById("score");
    const skills = document.getElementById("skills");

    // Validate resume
    if (!resumeInput.files.length) {
        alert("Please upload your resume PDF.");
        return;
    }

    // Validate job description
    if (!jobDescription.trim()) {
        alert("Please enter a job description.");
        return;
    }

    const resume = resumeInput.files[0];

    // Show loading state
    score.innerText = "Analyzing...";
    skills.innerHTML = `
        <p>🔍 Analyzing your resume...</p>
    `;

    const formData = new FormData();

    formData.append("resume", resume);
    formData.append("job_description", jobDescription);

    try {

        const response = await fetch(
            "https://bug-free-space-halibut-5vxrw9v4qr5ph46jx-8000.app.github.dev/analyze",
            {
                method: "POST",
                body: formData
            }
        );

        if (!response.ok) {
            throw new Error("Analysis failed.");
        }

        const data = await response.json();

        // Display score
        score.innerText =
            `Match Score: ${data.match_score}%`;

        // Display skills
        skills.innerHTML = `
            <h3>✓ Matched Skills</h3>

            <ul>
                ${
                    data.matched_skills.length
                    ? data.matched_skills
                        .map(skill => `<li>✓ ${skill}</li>`)
                        .join("")
                    : "<li>No matched skills found.</li>"
                }
            </ul>

            <h3>⚠ Missing Skills</h3>

            <ul>
                ${
                    data.missing_skills.length
                    ? data.missing_skills
                        .map(skill => `<li>⚠ ${skill}</li>`)
                        .join("")
                    : "<li>No missing skills.</li>"
                }
            </ul>
        `;

    } catch (error) {

        console.error(error);

        score.innerText = "Analysis failed";

        skills.innerHTML = `
            <p>
                ❌ Unable to connect to the AI Resume Analyzer.
                Please make sure the backend is running.
            </p>
        `;
    }
}
