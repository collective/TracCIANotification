= Subversion Location =

== Description ==

Adds a Subversion Location link to the contextual navigation under Browse Source. The link points to the Subversion URL for the folder you're viewing. This is very handy for making checkouts and such.

== Installation ==

Follow the normal [http://trac.edgewall.org/wiki/TracPlugins egg installation procedures].

Under the [components] section, enable the plugin:

{{{
[components]
subversionlocation.* = enabled
}}}

Finally, add a section to your project's trac.ini:

{{{
[svn]
repository_url = https://your.repository/location
}}}

Drink, and enjoy.

== Author ==

Subversion Location is written by Erik Rose and based on jhammel's [http://trac-hacks.org/wiki/SvnUrlsPlugin SvnUrlsPlugin]. Thanks, jhammel!

== Version History ==

 1.0.1::
  * No longer keeps the Browse Source tab from highlighting properly. Thanks to Jeremie Allard for the patch!
  * Removed egg dependency on Genshi, which we really don't require.
 1.0::
  Initial release