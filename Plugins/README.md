# Kibana Plugins
  To provide better integration and compatibility, i have 2 version of the same plugin. v8.10.4 is the latest stable release (as of Nov'23).

# Installation
  -> Download the version that is suitable for your kibana.  
  -> Run the command 
  ```
  \bin\kibana_plugin.bat install file:///<path to where you have kept the zip file>"
  ```

# Troubleshooting
  -> If your kibana doesnt start after the installation of the plugin and shows a message "Elastic did not start properly. Check you server logs", don't worry. Go into the kibana root folder > plugins > visevent > target > public and delete both the '.br' files. After this your kibana should start without any problem
  
  -> The current version aren't CSP supported, so if its just your project build and not a actual real production environment, you can turn off the CSP by adding the following lines to the kibana.yml file.
  ```
  csp.strict: false
  csp.warnLegacyBrowsers: false
  csp.script_src: ['unsafe-eval','unsafe-inline','self']
  ```

  # WARNING - Turning of CSP is not recommended and can lead to code injections and other vulnerabilities.