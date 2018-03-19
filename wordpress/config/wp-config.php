<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/Editing_wp-config.php
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'wpdb');

/** MySQL database username */
define('DB_USER', 'root');

/** MySQL database password */
define('DB_PASSWORD', 'password');

/** MySQL hostname */
define('DB_HOST', 'wordpress_db');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8');

/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         '6f05826213d6c3a959672b9b9359d4a0d9e9a72b');
define('SECURE_AUTH_KEY',  '6309836e2793c2de4a07ec3ef3fe84c325e77ad8');
define('LOGGED_IN_KEY',    '2cd77a305b040b5e420501d187302bb2222b72bd');
define('NONCE_KEY',        '1943624d6b9518cc47c5707e3899faeb86de83f6');
define('AUTH_SALT',        '85c124d7ebcd0000c3b6cd8bf91b4678c49357fa');
define('SECURE_AUTH_SALT', '4e3e490a80a1f13db4b41645c90f6837bd2b7ac5');
define('LOGGED_IN_SALT',   'b21d6bdcc8d3ed12318a1ad1b384d7ebfd97d4d3');
define('NONCE_SALT',       '101ada4ea68e1187869e1dbb014f5c35ad14e52a');
define('FS_METHOD',        'direct');
define('WP_HOME',          'http://'. $_SERVER['SERVER_NAME']. '/wordpress/' );
define('WP_SITEURL',       'http://'. $_SERVER['SERVER_NAME']. '/wordpress/' );
$_SERVER['REQUEST_URI'] = str_replace("/wp-admin/", "/wordpress/wp-admin/",  $_SERVER['REQUEST_URI']);

// Custom content directory
define( 'WP_CONTENT_DIR',  dirname( __FILE__ ) . '/wp-content' );
define( 'WP_CONTENT_URL',  'http://' . $_SERVER['SERVER_NAME'] . '/wordpress/wp-content' );
// Custom plugin directory
//define( 'WP_PLUGIN_DIR',   dirname( __FILE__ ) . '/wp-plugins' );
//define( 'WP_PLUGIN_URL',   'http://' . $_SERVER['HTTP_HOST'] . '/wordpress/wp-plugins' );
// Custom mu plugin directory
//define( 'WPMU_PLUGIN_DIR', dirname( __FILE__ ) . '/wpmu-plugins' );
//define( 'WPMU_PLUGIN_URL', 'http://' . $_SERVER['HTTP_HOST'] . '/wordpress/wpmu-plugins' );


//
/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix  = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the Codex.
 *
 * @link https://codex.wordpress.org/Debugging_in_WordPress
 */
define('WP_DEBUG', true);

// If we're behind a proxy server and using HTTPS, we need to alert Wordpress of that fact
// see also http://codex.wordpress.org/Administration_Over_SSL#Using_a_Reverse_Proxy
if (isset($_SERVER['HTTP_X_FORWARDED_PROTO']) && $_SERVER['HTTP_X_FORWARDED_PROTO'] === 'https') {
	$_SERVER['HTTPS'] = 'on';
}

// log php errors
@ini_set('log_errors','On'); // enable or disable php error logging (use 'On' or 'Off')
@ini_set('display_errors','Off'); // enable or disable public display of errors (use 'On' or 'Off')
@ini_set('error_log','/var/www/html/ wp-logs.log'); // path to server-writable log file
/* That's all, stop editing! Happy blogging. */

/** Absolute path to the WordPress directory. */
if ( !defined('ABSPATH') )
	define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');
