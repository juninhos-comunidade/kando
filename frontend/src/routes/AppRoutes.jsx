import { Routes, Route, Navigate } from "react-router-dom";

import Login from "../pages/Login";
import Signup from "../pages/Signup";
import Dashboard from "../pages/Dashboard";
import UploadProfile from "../pages/UploadProfile";
import ProfileScore from "../pages/ProfileScore";
import SimulationInstructions from "../pages/SimulationInstructions";
import SimulationQuestions from "../pages/SimulationQuestions";
import Report from "../pages/Report";
import TalentPassport from "../pages/TalentPassport";
import StudyPath from "../pages/StudyPath";

export default function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/login" replace />} />
      <Route path="/login" element={<Login />} />
      <Route path="/signup" element={<Signup />} />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="/upload" element={<UploadProfile />} />
      <Route path="/score" element={<ProfileScore />} />
      <Route
        path="/simulation/instructions"
        element={<SimulationInstructions />}
      />
      <Route path="/simulation/questions" element={<SimulationQuestions />} />
      <Route path="/report" element={<Report />} />
      <Route path="/talent-passport" element={<TalentPassport />} />
      <Route path="/study-path" element={<StudyPath />} />
    </Routes>
  );
}
