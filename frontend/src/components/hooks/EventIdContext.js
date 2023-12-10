import React, { createContext, useContext, useState } from 'react';

const EventIdContext = createContext();

export function EventIdProvider({ children }) {
  const [eventId, setEventId] = useState(1);

  return (
    <EventIdContext.Provider value={{ eventId, setEventId }}>
      {children}
    </EventIdContext.Provider>
  );
}

export function useEventId() {
    const context = useContext(EventIdContext);
    if (context === undefined) {
      throw new Error('useEventId must be used within a EventIdProvider');
    }
    return context;
  }