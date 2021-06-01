---
template: home.html
hide:
    - navigation
    - toc
---

Welcome to the Flipper Zero Docsss.

The main page is still in a WIP state.

Use tabs and sidebar to navigate.

<ul class="home-menu">
    {% for nav_item in config.extra.home %}
      <li>
        <aside>
          {{ '<img src="assets/home/%s">' % nav_item.img }}
        </aside>

        <main>
          <h2>{{ nav_item.title.en }}</h2>
          <ul class="home-submenu">
          {% for item in nav_item.children %}
            <li>
              <a href="{{ item.path }}">{{ item.title.en }}</a>
            </li>
          {% endfor %}
          </ul>
        </main>
      </li>
    {% endfor %}
</ul>
