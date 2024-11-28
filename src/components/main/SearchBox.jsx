import React from 'react';

export default function SearchBox() {
  return (
    <input
      type="text"
      placeholder="Search..."
      className="w-full p-4 text-gray-800 bg-white shadow-lg rounded-lg focus:ring-2 focus:ring-blue-600 focus:outline-none transition"
    />
  );
}
