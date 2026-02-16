// data-foundry-selector.js
// Add this script to your Jekyll site (e.g., in assets/js/)

(function () {
    'use strict';
    console.log('Data Foundry selector script loaded');
    // Cookie helper functions
    function setCookie(name, value, days = 365) {
        const d = new Date();
        d.setTime(d.getTime() + (days * 24 * 60 * 60 * 1000));
        const expires = "expires=" + d.toUTCString();
        document.cookie = name + "=" + value + ";" + expires + ";path=/";
    }

    function getCookie(name) {
        const nameEQ = name + "=";
        const ca = document.cookie.split(';');
        for (let i = 0; i < ca.length; i++) {
            let c = ca[i];
            while (c.charAt(0) === ' ') c = c.substring(1, c.length);
            if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
        }
        return null;
    }

    // Create modal HTML
    function createModal() {
        const modalHTML = `
      <div id="df-modal" style="display: none; position: fixed; z-index: 10000; left: 0; top: 0; width: 100%; height: 100%; overflow: auto; background-color: rgba(0,0,0,0.4);">
        <div style="background-color: #fefefe; margin: 15% auto; padding: 20px; border: 1px solid #888; border-radius: 8px; width: 90%; max-width: 500px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
          <h2 id="df-modal-title" style="margin-top: 0; color: #333;">Select Data Foundry Instance</h2>
          <div id="df-modal-content"></div>
          <div style="margin-top: 20px; text-align: right;">
            <button id="df-cancel-btn" style="padding: 8px 16px; margin-right: 8px; background-color: #6c757d; color: white; border: none; border-radius: 4px; cursor: pointer;">Cancel</button>
            <button id="df-confirm-btn" style="padding: 8px 16px; background-color: #4DAF50; color: white; border: none; border-radius: 4px; cursor: pointer;">Confirm</button>
          </div>
        </div>
      </div>
    `;

        document.body.insertAdjacentHTML('beforeend', modalHTML);
    }

    // Show modal for first-time selection
    function showInitialModal(instances, callback) {
        const modal = document.getElementById('df-modal');
        const title = document.getElementById('df-modal-title');
        const content = document.getElementById('df-modal-content');

        title.textContent = 'Enter Data Foundry Instance URL';

        let optionsHTML = '<p style="margin-bottom: 15px; color: #666;">Enter the URL for your Data Foundry instance:</p>';
        optionsHTML += '<input type="text" id="df-instance-input" placeholder="https://datafoundry.example.com" style="width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 4px; font-size: 14px; box-sizing: border-box;">';

        content.innerHTML = optionsHTML;

        modal.style.display = 'block';

        // Focus the input
        setTimeout(() => {
            document.getElementById('df-instance-input').focus();
        }, 100);

        const confirmBtn = document.getElementById('df-confirm-btn');
        const cancelBtn = document.getElementById('df-cancel-btn');

        confirmBtn.onclick = function () {
            const input = document.getElementById('df-instance-input');
            const url = input.value.trim();

            if (!url) {
                alert('Please enter a valid URL');
                return;
            }

            // Remove trailing slash if present
            const cleanUrl = url.replace(/\/$/, '');

            modal.style.display = 'none';
            callback({ name: cleanUrl, url: cleanUrl });
        };

        cancelBtn.onclick = function () {
            modal.style.display = 'none';
        };

        // Allow Enter key to confirm
        document.getElementById('df-instance-input').addEventListener('keypress', function (e) {
            if (e.key === 'Enter') {
                confirmBtn.click();
            }
        });
    }

    // Show modal for confirmation with inline editable instance + SVG pencil icon
    function showConfirmationModal(savedInstance, instances, callback) {
        const modal = document.getElementById('df-modal');
        const title = document.getElementById('df-modal-title');
        const content = document.getElementById('df-modal-content');

        title.textContent = 'Confirm Navigation';

        // SVG pencil icon (inline, grayscale)
        const pencilSVG = `
            <svg id="df-edit-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
                width="18" height="18" fill="none" stroke="#999" stroke-width="2"
                stroke-linecap="round" stroke-linejoin="round"
                style="margin-left: 8px; transition: stroke 0.2s;">
            <path d="M12 20h9" />
            <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4 12.5-12.5z" />
            </svg>
  `;

        let contentHTML = `
    <p style="margin-bottom: 15px; color: #666;">Navigate to your saved instance?</p>
    <div id="df-instance-display"
         style="display: flex; align-items: center; background-color: #f8f9fa; padding: 12px; border-radius: 4px; margin-bottom: 10px; cursor: pointer; border: 1px solid transparent; transition: border 0.2s, background-color 0.2s;">
      <strong id="df-instance-text" style="flex: 1; word-break: break-all;">${savedInstance.url}</strong>
      ${pencilSVG}
    </div>
    <p style="font-size: 13px; color: #888; margin-top: -5px;">Click the instance above to edit.</p>
  `;

        content.innerHTML = contentHTML;
        modal.style.display = 'block';

        const displayDiv = document.getElementById('df-instance-display');
        const instanceText = document.getElementById('df-instance-text');
        const editIcon = document.getElementById('df-edit-icon');

        // Hover feedback
        displayDiv.addEventListener('mouseenter', () => {
            displayDiv.style.border = '1px solid #ddd';
            editIcon.style.stroke = '#666';
        });
        displayDiv.addEventListener('mouseleave', () => {
            if (displayDiv.getAttribute('contenteditable') !== 'true') {
                displayDiv.style.border = '1px solid transparent';
            }
            editIcon.style.stroke = '#999';
        });

        // Start editing (click box or icon)
        function startEditing() {
            if (displayDiv.getAttribute('contenteditable') === 'true') return;
            displayDiv.setAttribute('contenteditable', 'true');
            displayDiv.style.border = '1px solid #4DAF50';
            displayDiv.style.backgroundColor = '#fff';
            editIcon.style.stroke = '#4DAF50';
            displayDiv.focus();

            // Move caret to end of text
            const range = document.createRange();
            range.selectNodeContents(instanceText);
            range.collapse(false);
            const sel = window.getSelection();
            sel.removeAllRanges();
            sel.addRange(range);
        }

        displayDiv.addEventListener('click', startEditing);
        editIcon.addEventListener('click', (e) => {
            e.stopPropagation();
            startEditing();
        });

        // Stop editing on Enter or blur
        displayDiv.addEventListener('keypress', function (e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                displayDiv.blur();
            }
        });

        displayDiv.addEventListener('blur', function () {
            displayDiv.removeAttribute('contenteditable');
            displayDiv.style.border = '1px solid transparent';
            displayDiv.style.backgroundColor = '#f8f9fa';
            editIcon.style.stroke = '#999';
        });

        const confirmBtn = document.getElementById('df-confirm-btn');
        const cancelBtn = document.getElementById('df-cancel-btn');

        confirmBtn.onclick = function () {
            const newUrl = instanceText.textContent.trim();
            if (!newUrl) {
                alert('Please enter a valid URL');
                return;
            }
            const cleanUrl = newUrl.replace(/\/$/, '');
            const selectedInstance = { name: cleanUrl, url: cleanUrl };
            modal.style.display = 'none';
            callback(selectedInstance);
        };

        cancelBtn.onclick = function () {
            modal.style.display = 'none';
        };
    }

    // Initialize
    function init() {
        console.log('Init function called');
        createModal();

        const dfLinks = document.querySelectorAll('a.df-link, a[data-df-link]');
        console.log('Found df-links:', dfLinks.length, dfLinks);
        dfLinks.forEach(link => {
            link.addEventListener('click', function (e) {
                e.preventDefault();

                const savedInstanceData = getCookie('df-instance');
                const relativePath = this.getAttribute('data-df-path') || '/';

                if (savedInstanceData) {
                    // Parse saved instance
                    const savedInstance = JSON.parse(savedInstanceData);

                    // Show confirmation modal
                    showConfirmationModal(savedInstance, null, function (selectedInstance) {
                        setCookie('df-instance', JSON.stringify(selectedInstance));
                        window.open(selectedInstance.url + relativePath, '_blank');
                    });
                } else {
                    // First time - show selection modal
                    showInitialModal(null, function (selectedInstance) {
                        setCookie('df-instance', JSON.stringify(selectedInstance));
                        window.open(selectedInstance.url + relativePath, '_blank');
                    });
                }
            });
        });
    }

    // Run when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();