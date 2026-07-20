import { useState, useEffect } from "react";

export default function useAuth() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    setIsAuthenticated(!!localStorage.getItem("kando_user"));
  }, []);

  return { isAuthenticated };
}
