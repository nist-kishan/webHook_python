import React, { useEffect, useState } from "react";
import axios from "axios";
import { GitCommit, GitPullRequest, GitMerge } from "lucide-react";

export default function App() {
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
        return `${event.author} opened a PR from ${event.from_branch} → ${event.to_branch} on ${date}`;
      case "merge":
        return `${event.author} merged ${event.from_branch} → ${event.to_branch} on ${date}`;
      default:
        return "Unknown event";
    }
  };

  const iconFor = (type) => {
    switch (type) {
      case "push":
        return <GitCommit className="w-5 h-5 text-emerald-500" />;
      case "pull_request":
        return <GitPullRequest className="w-5 h-5 text-indigo-500" />;
      case "merge":
        return <GitMerge className="w-5 h-5 text-fuchsia-600" />;
      default:
        return null;
    }
  };

  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-200 flex flex-col items-center py-10 px-4">
      <h1 className="text-4xl font-extrabold text-slate-800 mb-10 tracking-tight flex items-center gap-3">
        <GitCommit className="w-8 h-8 text-blue-600 animate-pulse" />
        GitHub Webhook Feed
      </h1>

      <section className="w-full max-w-3xl space-y-4">
        {events.length === 0 ? (
          <p className="text-center text-slate-500">No events yet – push something! 🚀</p>
        ) : (
          events.map((evt, i) => (
            <article
              key={`${evt.timestamp}-${i}`}
              className="flex items-start gap-3 p-4 bg-white/90 rounded-2xl shadow-md border border-slate-200 hover:shadow-lg transition-shadow"
            >
              {iconFor(evt.event_type)}
              <p className="text-sm text-slate-700 leading-relaxed">
                {renderMessage(evt)}
              </p>
            </article>
          ))
        )}
      </section>
    </main>
  );
}
