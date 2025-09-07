export function DataNovaIcon({ className }: { className?: string }) {
  return (
    <svg
      className={className}
      width="36"
      height="36"
      viewBox="0 0 24 24"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      {/* Simplified data connection icon */}
      <circle cx="12" cy="12" r="3" stroke="currentColor" strokeWidth="1.5" />
      <path d="M12 6L12 3" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" />
      <path d="M18 12L21 12" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" />
      <path d="M12 18L12 21" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" />
      <path d="M6 12L3 12" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" />
      <circle cx="12" cy="12" r="1" fill="currentColor" />
    </svg>
  );
}
