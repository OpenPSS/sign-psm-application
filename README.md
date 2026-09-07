# sign-psm-application
Github action to sign a PlayStaiton Mobile Application

example usage:
```
      - name: Sign Example PSM Game
        uses: OpenPSS/sign-psm-application
        with:
            input: test/PsmTestSuite
            output: test/PsmTestSuite-signed
            content_id: UM0999-NPNA99999_00-0000000000000000
```

