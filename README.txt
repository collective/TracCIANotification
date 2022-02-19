CIA Notfication

    Description

        Makes the CIA IRC bot announce new tickets.

    Installation

        Follow the normal egg installation procedures:
        https://trac.edgewall.org/wiki/TracPlugins.
        
        Stick stuff like this in trac.ini::
        
            [components]
            cianotification.* = enabled
            
            [notification]
            cia_project = MyCrazyProject
            cia_server = http://cia.navi.cx

        Then with your CIA.vc project set 'Advanced Filtering' to something like::

            <match path="/message/source/project">your project</match>
            <rule>
            <find path="/message/source/module">Issue tracker</find>
            <formatter medium="irc">
              <format appliesTo="CommitToIRC">
                  <b>New ticket: </b>
                  <autoHide><color fg='green'><author/></color></autoHide>
                  *
                  <autoHide><b>http://example.com/ticket/<revision/></b></autoHide>
                  <log/>
              </format>
            </formatter>
            <rule>
            </rule>
            <not><find path="/message/source/module">Issue tracker</find></not>
            <formatter medium="irc">
              <format appliesTo="CommitToIRC">
                  <b>Commit: </b>
                  <autoHide><color fg='green'><author/></color></autoHide>
                  <autoHide><color fg='orange'><branch/></color></autoHide>
                  *
                  <autoHide><b><version/></b></autoHide>
                  <autoHide><b>http://example.com/changeset/<revision/></b></autoHide>
                  <color fg='aqua'><module/></color>/<files/><b>:</b>
                  <log/>
              </format>
            </formatter>
            </rule>


    Author

        Wrapped in a nice Trac 0.11 wrapper by Erik Rose, based on wiggy's patch
        for 0.10: http://www.wiggy.net/files/trac-cia.diff.
