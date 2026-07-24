import "./Signup.css";

export default function Signup() {
  return (
    <div className="signup">
      <section className="signup__welcome">
        <div className="signup__welcome_logo">
          <svg
            className="signup__welcome_logo-img"
            xmlns="http://www.w3.org/2000/svg"
            width="1024"
            height="1024"
            viewBox="0 0 1024 1024"
          >
            <g>
              <path
                d="M 327.00 613.11 L 327.00 333.00 L 241.50 333.00 L 156.00 333.00 L 156.00 271.00 L 156.00 209.00 L 388.00 209.00 L 620.00 209.00 L 620.00 270.99 L 620.00 332.99 L 537.99 333.24 L 455.98 333.50 L 456.00 574.69 L 456.01 815.89 L 406.25 845.80 C378.89,862.25 350.44,879.42 343.03,883.97 C335.63,888.51 328.99,892.45 328.28,892.72 C327.24,893.12 327.00,840.55 327.00,613.11 ZM 475.00 584.61 L 475.00 363.00 L 539.00 363.00 L 603.00 363.00 L 603.00 439.00 L 603.00 515.00 L 647.78 515.00 C672.82,515.00 696.21,514.54 700.85,513.96 C738.83,509.20 767.84,483.40 778.20,445.18 C780.96,434.97 781.22,411.89 778.69,401.67 C770.51,368.72 746.22,344.09 713.82,335.90 C706.56,334.06 701.59,333.73 674.75,333.28 L 644.00 332.76 L 644.00 270.74 L 644.00 208.72 L 681.75 209.30 C722.87,209.94 733.63,210.94 753.36,215.92 C787.87,224.64 816.11,240.01 840.97,263.61 C877.63,298.41 900.61,345.30 907.06,398.50 C909.78,420.94 908.06,451.88 902.82,474.50 C887.30,541.49 837.08,595.90 772.77,615.40 C743.09,624.39 725.56,626.00 657.04,626.00 L 603.02 626.00 L 602.76 677.58 L 602.50 729.16 L 569.00 749.34 C493.41,794.88 479.53,803.26 477.32,804.71 L 475.00 806.23 L 475.00 584.61 Z"
                fill="currentColor"
              />
            </g>
          </svg>
          <h1 className="signup__welcome_logo-title">Talent Passport</h1>
        </div>
        <div className="signup__welcome_intro">
          <h2 className="signup__welcome_intro_subtitle">
            Quão pronto você está pro seu emprego dos sonhos?
          </h2>
          <p className="signup__welcome_intro_text">
            Junte-se e transforme o sonho em realidade.
          </p>
        </div>
        <div className="signup__welcome_instructions">
          <div className="signup__welcome_instructions_list-numbers">
            <p className="signup__welcome_instructions_list-number">1</p>
            <p className="signup__welcome_instructions_list-number">2</p>
            <p className="signup__welcome_instructions_list-number">3</p>
          </div>
          <div className="signup__welcome_instructions_list-texts">
            <p className="signup__welcome_instructions_list-text">
              Envie seu perfil
            </p>
            <p className="signup__welcome_instructions_list-text">
              Faça a simulação
            </p>
            <p className="signup__welcome_instructions_list-text">
              Estude com trilha personalizada
            </p>
          </div>
        </div>
      </section>
      <section className="signup__form">
        <p className="signup__title">Criar conta</p>
        <form action="" className="signup__form_inputs">
          <input
            type="email"
            className="signup__form_email"
            placeholder="Email"
          />
          <input
            type="password"
            className="signup__form_password"
            placeholder="Senha"
          />
          <button className="signup__form_button">Criar conta</button>
          <div className="signup__create-account">
            <p className="signup__account">Já tem conta?</p>
            <a href="" className="signup__account_link">
              Entrar
            </a>
          </div>
        </form>
        <div className="signup__divider">
          <span className="signup__divider_text">ou</span>
        </div>
        <button className="signup__google_button">
          <svg
            className="signup__google_button-icon"
            viewBox="-3 0 262 262"
            xmlns="http://www.w3.org/2000/svg"
            preserveAspectRatio="xMidYMid"
            fill="#000000"
          >
            <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
            <g
              id="SVGRepo_tracerCarrier"
              stroke-linecap="round"
              stroke-linejoin="round"
            ></g>
            <g id="SVGRepo_iconCarrier">
              <path
                d="M255.878 133.451c0-10.734-.871-18.567-2.756-26.69H130.55v48.448h71.947c-1.45 12.04-9.283 30.172-26.69 42.356l-.244 1.622 38.755 30.023 2.685.268c24.659-22.774 38.875-56.282 38.875-96.027"
                fill="#4285F4"
              ></path>
              <path
                d="M130.55 261.1c35.248 0 64.839-11.605 86.453-31.622l-41.196-31.913c-11.024 7.688-25.82 13.055-45.257 13.055-34.523 0-63.824-22.773-74.269-54.25l-1.531.13-40.298 31.187-.527 1.465C35.393 231.798 79.49 261.1 130.55 261.1"
                fill="#34A853"
              ></path>
              <path
                d="M56.281 156.37c-2.756-8.123-4.351-16.827-4.351-25.82 0-8.994 1.595-17.697 4.206-25.82l-.073-1.73L15.26 71.312l-1.335.635C5.077 89.644 0 109.517 0 130.55s5.077 40.905 13.925 58.602l42.356-32.782"
                fill="#FBBC05"
              ></path>
              <path
                d="M130.55 50.479c24.514 0 41.05 10.589 50.479 19.438l36.844-35.974C195.245 12.91 165.798 0 130.55 0 79.49 0 35.393 29.301 13.925 71.947l42.211 32.783c10.59-31.477 39.891-54.251 74.414-54.251"
                fill="#EB4335"
              ></path>
            </g>
          </svg>
          Continuar com o Google
        </button>
      </section>
    </div>
  );
}
