/* ===========================================================
 * JFreeChart : a free chart library for the Java(tm) platform
 * ===========================================================
 *
 * (C) Copyright 2000-2004, by Object Refinery Limited and Contributors.
 *
 * Project Info:  http://www.jfree.org/jfreechart/index.html
 *
 * This library is free software; you can redistribute it and/or modify it under the terms
 * of the GNU Lesser General Public License as published by the Free Software Foundation;
 * either version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
 * without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License along with this
 * library; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330,
 * Boston, MA 02111-1307, USA.
 *
 * [Java is a trademark or registered trademark of Sun Microsystems, Inc. 
 * in the United States and other countries.]
 *
 * --------------------
 * XYZURLGenerator.java
 * --------------------
 * (C) Copyright 2003, by Object Refinery Limited and Contributors.
 *
 * Original Author:  David Gilbert (for Object Refinery Limited);
 * Contributors:     -;
 *
 * $Id: XYZURLGenerator.java,v 1.4 2004/01/05 17:11:51 mungady Exp $
 *
 * Changes:
 * --------
 * 03-Feb-2003 : Version 1 (DG);
 *
 */

package org.jfree.chart.urls;

import org.jfree.data.XYZDataset;

/**
 * Interface for a URL generator for plots that uses data from an {@link XYZDataset}.
 *
 * @author David Gilbert
 */
public interface XYZURLGenerator extends XYURLGenerator {

    /**
     * Generates a URL for a particular item within a series.
     *
     * @param data  the dataset.
     * @param series  the series index (zero-based).
     * @param item  the item index (zero-based).
     *
     * @return a string containing the generated URL.
     */
    public String generateURL(XYZDataset data, int series, int item);

}
