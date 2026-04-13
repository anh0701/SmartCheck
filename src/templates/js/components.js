class AppMenu extends HTMLElement {
  async connectedCallback() {
    const res = await fetch('/src/templates/components/menu.html');
    const html = await res.text();

    this.attachShadow({ mode: 'open' }); // tránh leak CSS
    this.shadowRoot.innerHTML = html;
  }
}

customElements.define('app-menu', AppMenu);