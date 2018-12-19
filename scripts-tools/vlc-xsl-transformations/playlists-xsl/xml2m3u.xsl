<xsl:stylesheet xmlns:xsl = "http://www.w3.org/1999/XSL/Transform" version = "1.0" >
    <xsl:output omit-xml-declaration="yes" method="text" indent="no" encoding="UTF-8" />
    <xsl:template match = "/root" > 
        <xsl:text>#EXTM3U</xsl:text>
        <xsl:for-each select="row">
#EXTINF: -1 , <xsl:value-of select="snippet/title" />
<xsl:text>
</xsl:text>
https://www.youtube.com/watch?v=<xsl:value-of select="contentDetails/videoId" />
<xsl:text> 
</xsl:text>            
        </xsl:for-each>           
    </xsl:template>
</xsl:stylesheet>