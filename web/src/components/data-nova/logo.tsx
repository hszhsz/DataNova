// Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
// SPDX-License-Identifier: MIT

import Link from "next/link";

export function Logo() {
  return (
    <Link
      className="opacity-70 transition-opacity duration-300 hover:opacity-100 flex items-center gap-3"
      href="/"
    >
      <svg 
        width="36" 
        height="36" 
        viewBox="0 0 24 24" 
        fill="none" 
        xmlns="http://www.w3.org/2000/svg"
        className="text-blue-500"
      >
        {/* Simplified data connection icon */}
        <circle cx="12" cy="12" r="3" stroke="currentColor" strokeWidth="1.5" />
        <path d="M12 6L12 3" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" />
        <path d="M18 12L21 12" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" />
        <path d="M12 18L12 21" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" />
        <path d="M6 12L3 12" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" />
        <circle cx="12" cy="12" r="1" fill="currentColor" />
      </svg>
      <span className="font-bold text-xl bg-gradient-to-r from-blue-500 to-purple-600 bg-clip-text text-transparent">
        DataNova
      </span>
    </Link>
  );
}