<xsl:stylesheet xmlns:xsl = "http://www.w3.org/1999/XSL/Transform" version = "1.0" >
    <xsl:output omit-xml-declaration="no" media-type="application/xspf+xml"
        method="xml" indent="yes" encoding="UTF-8" /> 
    <xsl:strip-space elements="*"/>
    <xsl:template match = "/root" > 
        <playlist version="1" xmlns="http://xspf.org/ns/0/">
            <title>YouTube Playlist</title>
            <creator>Yannis</creator>
            <trackList>
                <xsl:for-each select="row">
                    <track>
                        <location>https://www.youtube.com/watch?v=<xsl:value-of select="contentDetails/videoId" /></location>
                        <title><xsl:value-of select="snippet/title" /></title>
                        <annotation><xsl:value-of select="snippet/title" /></annotation>    
                        <image><xsl:value-of select="snippet/thumbnails/default/url" /></image>                        
                    </track>
                </xsl:for-each>
            </trackList>
        </playlist>

    </xsl:template>
</xsl:stylesheet>