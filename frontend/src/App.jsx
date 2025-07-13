import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    fetchEvents();
    const interval = setInterval(fetchEvents, 15000);
    return () => clearInterval(interval);
  }, []);

  const fetchEvents = async () => {
    try {
      const res = await axios.get("http://localhost:5000/events");
      setEvents(res.data);
    } catch (err) {
      console.error("Error fetching events:", err);
    }
  };

  const renderMessage = (event) => {
    const date = new Date(event.timestamp).toLocaleString("en-GB", {
      timeZone: "UTC",
      hour12: true,
    });

    switch (event.event_type) {
      case "push":
        return `${event.author} pushed to ${event.to_branch} on ${date}`;
      case "pull_request":
        return `${event.author} submitted a pull request from ${event.from_branch} to ${event.to_branch} on ${date}`;
      case "merge":
        return `${event.author} merged branch ${event.from_branch} to ${event.to_branch} on ${date}`;
      default:
        return "Unknown event";
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold text-center text-blue-600 mb-8">GitHub Webhook Events</h1>
      <div className="max-w-2xl mx-auto space-y-4">
        {events.length === 0 ? (
          <p className="text-gray-500 text-center">No events found.</p>
        ) : (
          events.map((event, index) => (
            <div key={index} className="bg-white p-4 rounded-xl shadow border border-gray-200">
              <p className="text-sm text-gray-700">{renderMessage(event)}</p>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default App;
