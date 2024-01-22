import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';
// import styles from 'src/theme/CodeBlock/Line/styles.module.css';
export default function CodeBlockLine({
  line,
  classNames,
  showLineNumbers,
  getLineProps,
  getTokenProps,
}) {
  if (line.length === 1 && line[0].content === '\n') {
    line[0].content = '';
  }

  // return if the line starts with '>' 
  const [startsWithPrefix1, shift1] = checkPrefix('>')

  let startsWithPrefix2 = false;
  let shift2 = 0;
  let modifiedLine = [...line];

  if (startsWithPrefix1) {
    // returns line without '>>> '
    modifiedLine = getModifiedLine1(shift1)
  } else {
    // check if the line starts with '$'
    [startsWithPrefix2, shift2] = checkPrefix('$')
    if (startsWithPrefix2) {
      // returns line without '$ '
      modifiedLine = getModifiedLine2(shift2)
    }
  }
  
  // '>>>' may be contained in one, two or three tokens of the line (let's call them target tokens)
  // and the ' ' may be stored in the last of these tokens or in the token after the last
  function checkPrefix(sign) {
    let isHasPref = false;
    let shift = 0
    if (line.length > 0 && line[0].content.startsWith(sign)) {
      isHasPref= true
      shift = 0
    } else {
      // the 0th token of the line may content only '' due to the condition from the beginning of the function
      // then the search of the target tokens should be shifted by 1
      if (line.length > 1 && line[0].content=='' && line[1].content.startsWith(sign)) {
        isHasPref = true
        shift = 1
      }
    }
    return [isHasPref, shift]
  }

  function getModifiedLine1(shift) {
    // remove '>>> '
    let par = [...line]
    let k = -1; //variable to store the index of the last target token
    let i = 0 + shift; // token index
    let j = 0; // token content index
    let n = 0; //number of '>' in token

    // check first three tokens
    while ((i < line.length) && (i < (3+shift))) {
      j = 0; 
      n = 0; 

      // check the content of the each token
      while ((j < line[i].content.length) && (j < (3+shift-i))) {
        if (line[i].content[j] == '>') {
          n++; // if find '>' in the token content, record the number of '>'
        } else {
          break
        }
        j++;
      }

      // if there were '>' in token content, remove them
      if (n > 0) {
        par[i] = {...line[i], content: line[i].content.substring(n)};
        // record the token which has the last part of '>>>' to remove ' '
        k = i; //assign the index of the token to have the index of the last target token in the end
      }
      i++;
    }

    // in the last token that was cleaned from the '>', check if it now has ' ' in the beginning and remove it:
    if (k >= 0) {
      if (par[k].content.length > 0 && par[k].content[0] == ' ') {
        par[k] = {...par[k], content: par[k].content.substring(1)};
      } else {
        // or if the ' ' in the next token, remove it from there:
        if (par.length > k && par[k+1].content.length > 0 && par[k+1].content[0] == ' ') {
          par[k+1] = {...par[k+1], content: par[k+1].content.substring(1)};
        }
      }
    }
    // return cleaned from the '>>> ' line and true, if line contained '>>> '
    // otherwise, line itself and false
    return par
  }

  function getModifiedLine2(shift) {
    // remove '$', it is in the first or in the second token
    let par = [...line]
    let i = 0 + shift; // token index

    par[i] = {...line[i], content: line[i].content.substring(1)};

    // check if the token now has ' ' in the beginning and remove it:
    if (par[i].content.length > 0 && par[i].content[0] == ' ') {
      par[i] = {...par[i], content: par[i].content.substring(1)};
    } else {
      // or if the ' ' in the next token, remove it from there:
      if (par.length > i && par[i+1].content.length > 0 && par[i+1].content[0] == ' ') {
        par[i+1] = {...par[i+1], content: par[i+1].content.substring(1)};
      }
    }

    // return cleaned from the '$ ' line
    return par
  }

  const lineProps = getLineProps({
    modifiedLine,
    className: clsx(classNames, showLineNumbers && styles.codeLine),
  });

  const lineTokens = modifiedLine.map((token, key) => (
    <span key={key} {...getTokenProps({token, key})} />
  ));

  return (
    <span {...lineProps}>
      {showLineNumbers ? (
        <>
        {startsWithPrefix1 ? (
          <>
          <span className={styles.unselectablePrefix}>{'>>> '}</span> 
          </>
          ) : (
            <>
            {startsWithPrefix2 ? (
              <>
              <span className={styles.unselectablePrefix}>{'$ '}</span> 
              </>
            ) : (
              <>
              </>
              )
            }
            </>
          )
        }
          <span className={styles.codeLineNumber} />
          <span className={styles.codeLineContent}>{lineTokens}</span>
        </>
      ) : (
        <>
          {startsWithPrefix1 ? (
          <>
          <span className={styles.unselectablePrefix}>{'>>> '}</span> 
          </>
          ) : (
            <>
            {startsWithPrefix2 ? (
              <>
              <span className={styles.unselectablePrefix}>{'$ '}</span> 
              </>
            ) : (
              <>
              </>
              )
            }
            </>
          )
          }
          {lineTokens}
        </>
      )}
      <br />
    </span>
  );
}
