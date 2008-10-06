/*
VisAD system for interactive analysis and visualization of numerical
data.  Copyright (C) 1996 - 2008 Bill Hibbard, Curtis Rueden, Tom
Rink, Dave Glowacki, Steve Emmerson, Tom Whittaker, Don Murray, and
Tommy Jasmin.

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Library General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Library General Public License for more details.

You should have received a copy of the GNU Library General Public
License along with this library; if not, write to the Free
Software Foundation, Inc., 59 Temple Place - Suite 330, Boston,
MA 02111-1307, USA
*/

package visad.data.visad.object;

import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;

import visad.data.visad.BinaryReader;
import visad.data.visad.BinaryWriter;

public class BinaryFloatMatrix
  implements BinaryObject
{
  public static final int computeBytes(float[][] matrix)
  {
    if (matrix == null) {
      return 4;
    }

    int len = 4;
    for (int i = 0; i < matrix.length; i++) {
      len += 4 + (matrix[i].length * 4);
    }

    return len;
  }

  public static final float[][] read(BinaryReader reader)
    throws IOException
  {
    DataInput file = reader.getInput();

    final int len = file.readInt();
if(DEBUG_RD_DATA)System.err.println("rdFltMtx: len (" + len + ")");
    if (len < 0) {
      return null;
    }

    float[][] matrix = new float[len][];
    for (int i = 0; i < len; i++) {
      final int len2 = file.readInt();
if(DEBUG_RD_DATA)System.err.println("rdFltMtx: #" + i + " len (" + len2 + ")");
      matrix[i] = new float[len2];
      for (int j = 0; j < len2; j++) {
        matrix[i][j] = file.readFloat();
if(DEBUG_RD_DATA_DETAIL)System.err.println("rdFltMtx: #" + i + "," + j +" (" + matrix[i][j] + ")");
      }
    }

    return matrix;
  }

  private static final boolean fasterButUglier = true;

  public static final void write(BinaryWriter writer, float[][] matrix,
                                 Object token)
    throws IOException
  {
    DataOutput file = writer.getOutput();

    if (matrix == null) {
if(DEBUG_WR_DATA)System.err.println("wrFltMtx: null (" + -1 + ")");
      file.writeInt(-1);
    } else {
      if (fasterButUglier) {
        byte[] buf = new byte[4+matrix.length*(4+4*matrix[0].length)];
        int bufIdx = 0;

if(DEBUG_WR_DATA)System.err.println("wrFltMtx: row len (" + matrix.length + ")");
        for (int b = 3, l = matrix.length; b >= 0; b--) {
          buf[bufIdx + b] = (byte )(l & 0xff);
          l >>= 8;
        }
        bufIdx += 4;

        for (int i = 0; i < matrix.length; i++) {
          final int len = matrix[i].length;
if(DEBUG_WR_DATA)System.err.println("wrFltMtx: #" + i + " len (" + matrix[i].length + ")");
          for (int b = 3, l = len; b >= 0; b--) {
            buf[bufIdx + b] = (byte )(l & 0xff);
            l >>= 8;
          }
          bufIdx += 4;

          for (int j = 0; j < len; j++) {
if(DEBUG_WR_DATA_DETAIL)System.err.println("wrFltMtx: #" + i + "," + j + " (" + matrix[i][j] + ")");
            int x = Float.floatToIntBits(matrix[i][j]);
            for (int b = 3; b >= 0; b--) {
              buf[bufIdx + b] = (byte )(x & 0xff);
              x >>= 8;
            }
            bufIdx += 4;
          }
        }

        file.write(buf);
      } else { // !fasterButUglier
if(DEBUG_WR_DATA)System.err.println("wrFltMtx: row len (" + matrix.length + ")");
        file.writeInt(matrix.length);
        for (int i = 0; i < matrix.length; i++) {
          final int len = matrix[i].length;
if(DEBUG_WR_DATA)System.err.println("wrFltMtx: #" + i + " len (" + matrix[i].length + ")");
          file.writeInt(len);
          for (int j = 0; j < len; j++) {
if(DEBUG_WR_DATA_DETAIL)System.err.println("wrFltMtx: #" + i + "," + j + " (" + matrix[i][j] + ")");
            file.writeFloat(matrix[i][j]);
          }
        }
      }
    }
  }
}
