
export default function LoginLayout({ children }) {
  return (
    <section>
      <div className="min-h-screen flex">
        <h1 className="login-heading flex">Connect with a universe of mentors and peers, ready to uplift you.</h1>
        {children}
      </div>
    </section>
  );
}
