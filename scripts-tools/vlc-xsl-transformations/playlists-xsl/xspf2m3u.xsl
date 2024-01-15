<xsl:stylesheet xmlns:xsl = "http://www.w3.org/1999/XSL/Transform" xmlns:xspf="http://xspf.org/ns/0/" version = '1.0'>
    <xsl:output omit-xml-declaration="yes" method="text" indent="no" encoding="UTF-8" />
    <xsl:template match="/">
        <xsl:text>#EXTM3U</xsl:text>
        <xsl:for-each select="//xspf:trackList/xspf:track">
#EXTINF: -1 , <xsl:value-of select="./xspf:title"/> 
<xsl:text>
</xsl:text>
<xsl:value-of select="./xspf:location"/>
<xsl:text> 
</xsl:text>
        </xsl:for-each>
    </xsl:template>
</xsl:stylesheet>