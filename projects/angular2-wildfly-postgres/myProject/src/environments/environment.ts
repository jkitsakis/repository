// The file contents for the current environment will overwrite these during build.
// The build system defaults to the dev environment which uses `environment.ts`, but if you do
// `ng build --env=prod` then `environment.prod.ts` will be used instead.
// The list of which env maps to which file can be found in `angular-cli.json`.

export const environment = {
  production: false,
  SITE:'FR',
  SITE_URL:'http://192.168.235.130/dev', 
  A_URL:'http://192.168.235.130/dev', 
  B_URL:'http://192.168.235.130/dev', 
  C_URL:'http://192.168.235.130/dev', 
  D_URL:'http://192.168.235.130/dev', 
  DATE_TIME_FORMAT:'dd/MM/yyyy THH:mm',
  DATE_TIME:'dd/MM/yyyy',
  KEYCLOAK_JSON_LOCATION: "/static/cfg/transit/"
};
