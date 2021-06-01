---
template: home.html
hide:
    - navigation
    - toc
---

Добро пожаловать в документацию Flipper Zero.

Главная страница пока в разработке.

Используйте вкладки и боковое меню для навигации.

<ul class="home-menu">
    {% for nav_item in config.extra.home %}
      <li>
        <aside>
          {{ '<img src="assets/home/%s">' % nav_item.img }}
        </aside>

        <main>
          <h2>{{ nav_item.title.ru }}</h2>
          <ul class="home-submenu">
          {% for item in nav_item.children %}
            <li>
              <a href="{{ item.path }}">{{ item.title.ru }}</a>
            </li>
          {% endfor %}
          </ul>
        </main>
      </li>
    {% endfor %}
</ul>
