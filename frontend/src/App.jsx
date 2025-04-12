import React, { useState } from "react";
import axios from "axios";

const JobPredictionPage = () => {
  const [resume, setResume] = useState(null);
  const [resumeText, setResumeText] = useState("");
  const [loading, setLoading] = useState(false);
  const [skills, setSkills] = useState([]);
  const [jobs, setJobs] = useState([]);
  const [error, setError] = useState("");

  const handleResumeUpload = async (e) => {
    const formData = new FormData();
    formData.append("file", resume);

    setLoading(true);
    try {
      const response = await axios.post("http://localhost:5000/upload_resume", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setSkills(response.data.skills);
      setJobs(response.data.jobs);
    } catch (err) {
      setError("Error uploading resume");
    } finally {
      setLoading(false);
    }
  };

  const handleTextInput = async () => {
    setLoading(true);
    try {
      const response = await axios.post("http://localhost:5000/submit_text_resume", {
        resume_text: resumeText,
      });
      setSkills(response.data.skills);
      setJobs(response.data.jobs);
    } catch (err) {
      setError("Error processing resume text");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-blue-50 min-h-screen flex flex-col items-center py-8">
      <div className="max-w-4xl w-full bg-white rounded-lg shadow-lg p-8">
        <h1 className="text-3xl font-semibold text-center text-blue-700 mb-6">Job Prediction</h1>

        {/* Upload Resume Section */}
        <div className="text-center mb-6">
          <h2 className="text-2xl font-semibold text-blue-600 mb-4">Upload Your Resume</h2>
          <input
            type="file"
            onChange={(e) => setResume(e.target.files[0])}
            className="border border-blue-300 p-2 rounded-lg mb-4"
          />
          <br />
          <button
            onClick={handleResumeUpload}
            className="bg-blue-600 text-white py-2 px-6 rounded-lg mt-2"
            disabled={loading || !resume}
          >
            {loading ? "Uploading..." : "Upload Resume"}
          </button>
        </div>

        {/* Paste Resume Text Section */}
        <div className="text-center mb-6">
          <h2 className="text-2xl font-semibold text-blue-600 mb-4">Or Paste Resume Text</h2>
          <textarea
            placeholder="Paste your resume text here"
            value={resumeText}
            onChange={(e) => setResumeText(e.target.value)}
            className="border border-blue-300 p-4 rounded-lg w-full h-32 mb-4"
          />
          <br />
          <button
            onClick={handleTextInput}
            className="bg-blue-600 text-white py-2 px-6 rounded-lg mt-2"
            disabled={loading || !resumeText}
          >
            {loading ? "Processing..." : "Submit Resume Text"}
          </button>
        </div>

        {/* Error Message */}
        {error && <p className="text-red-500 text-center">{error}</p>}

        {/* Display Extracted Skills */}
        {skills.length > 0 && (
          <div className="mt-6">
            <h3 className="text-xl font-semibold text-blue-600 mb-2">Extracted Skills:</h3>
            <ul className="list-disc pl-5">
              {skills.map((skill, index) => (
                <li key={index} className="text-blue-700">{skill}</li>
              ))}
            </ul>
          </div>
        )}

        {/* Display Recommended Jobs */}
        {jobs.length > 0 && (
          <div className="mt-6">
            <h3 className="text-xl font-semibold text-blue-600 mb-2">Recommended Jobs:</h3>
            <div className="space-y-4">
              {jobs.map((job, index) => (
                <div key={index} className="border border-blue-200 p-4 rounded-lg shadow-sm">
                  <h4 className="font-bold text-blue-700">{job.title}</h4>
                  <p className="text-gray-700">{job.company}</p>
                  <p className="text-gray-600">{job.location}</p>
                  <p className="font-semibold text-blue-600">{job.salary}</p>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default JobPredictionPage;
