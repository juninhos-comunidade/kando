export default function Signup() {
  return (
    <>
      <section className="signup__welcome">
        <div className="signup__welcome_logo">
          <img src="" alt="" className="signup__welcome_logo-img" />
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
        <p className="signup__title"></p>
        <form action="" className="signup__form">
          <input
            type="email"
            className="signup__form_email"
            placeholder="Email"
          />
          <input
            type="password"
            className="signup__form_password"
            placeholder="Email"
          />
          <button className="signup__form_button">Criar conta</button>
          <div>
            <p className="signup__account">Já tem conta?</p>
            <a href="" className="signup__account_link">
              Entrar
            </a>
          </div>
        </form>
      </section>
    </>
  );
}
