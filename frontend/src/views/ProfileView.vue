<template>
    <base-auth-layout>
      <profile-form/>
    </base-auth-layout>
</template>

  <script>
  
  import ProfileForm from '@/components/ProfileForm.vue'
  import BaseAuthLayout from '@/layouts/BaseAuthLayout.vue'
  
  export default {
    name: "Profile",
    components: { ProfileForm, BaseAuthLayout }
  }
  
  </script>