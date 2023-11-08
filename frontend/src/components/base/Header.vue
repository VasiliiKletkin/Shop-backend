<template>
  <header class="py-3 mb-3 border-bottom">
    <div
      class="container-fluid d-grid gap-3 align-items-center"
      style="grid-template-columns: 1fr 2fr"
    >
      <div>
        <a
          href="#"
          class="d-flex align-items-center col-lg-4 mb-2 mb-lg-0 link-dark text-decoration-none dropdown-toggle"
          id="dropdownNavLink"
          aria-expanded="false"
        >
          <svg class="bi me-2" width="40" height="32">
            <use xlink:href="#bootstrap"></use>
          </svg>
        </a>
      </div>

      <div class="d-flex align-items-center">
        <form class="w-100 me-3">
          <input
            type="search"
            class="form-control"
            placeholder="Search..."
            aria-label="Search"
          />
        </form>
      </div>

      <b-nav-item-dropdown
        id="my-nav-dropdown"
        text="fff"
        toggle-class="nav-link-custom"
        right
      >
        <b-dropdown-item>1</b-dropdown-item>
        <b-dropdown-item>Two</b-dropdown-item>
        <b-dropdown-divider></b-dropdown-divider>
        <b-dropdown-item>Three</b-dropdown-item>
      </b-nav-item-dropdown>
    </div>
  </header>
  <div>
    <b-nav pills>
      <b-nav-item active>Вся продукция</b-nav-item>
      <b-nav-item>Коллекции</b-nav-item>
      <b-nav-item-dropdown
        id="my-nav-dropdown"
        text="Коллекции"
        toggle-class="nav-link-custom"
        right
      >
        <b-dropdown-item>One</b-dropdown-item>
        <b-dropdown-item>Two</b-dropdown-item>
        <b-dropdown-divider></b-dropdown-divider>
        <b-dropdown-item>Three</b-dropdown-item>
      </b-nav-item-dropdown>
    </b-nav>
  </div>
</template>

<script>
export default {
  name: "Header",
};
</script>

<style scoped>
/* Стили компонента */
</style>
