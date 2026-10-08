(() => {
  const sidebar = document.getElementById('sidebar');
  const toggle = document.getElementById('menuToggle');
  const scrim = document.getElementById('sidebarScrim');
  if (!sidebar || !toggle || !scrim) return;
  const close = () => { sidebar.classList.remove('open'); scrim.classList.remove('open'); };
  toggle.addEventListener('click', () => { sidebar.classList.add('open'); scrim.classList.add('open'); });
  scrim.addEventListener('click', close);
  sidebar.querySelectorAll('.side-link').forEach(link => link.addEventListener('click', () => {
    if (window.matchMedia('(max-width: 760px)').matches) close();
  }));
})();
